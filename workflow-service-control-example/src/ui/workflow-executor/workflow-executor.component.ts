import { Component, Inject, OnInit, OnDestroy } from '@angular/core';
import {
  Workflow,
  WorkflowsService,
  WorkflowInstancesService,
  WorkflowVariable,
  WorkflowInstance,
  WorkflowStartConfig,
} from '@cisco-msx/angular-api-client';
import { FetchState, poll } from '@cisco-msx/common';
import { BehaviorSubject, of, Observable, forkJoin, iif, throwError, Subscription, ReplaySubject, Subject } from 'rxjs';
import { filter, map, mergeMap, take, shareReplay, catchError, tap, takeUntil } from 'rxjs/operators';
import template from './workflow-executor.component.html';
import { createHelloWorldForm } from './hello-world.form';
import './workflow-executor.component.scss';

const workflowUniqueName = 'INSERT WORKFLOW UNIQUE NAME  HERE';
@Component({
  selector: 'wx-workflow-executor',
  host: {
    class: 'vms-standard-view wx-workflow-executor',
  },
  template
})
export class WorkflowExecutorComponent implements OnInit, OnDestroy {
  upload = {
    open: false
  }
  form = createHelloWorldForm();

  _workflowExecutionState: BehaviorSubject<FetchState> =
    new BehaviorSubject(FetchState.INITIAL);

  isExecuting$ = this._workflowExecutionState.pipe(map(state => state === FetchState.FETCHING));
  isFailure$ = this._workflowExecutionState.pipe(map(state => state === FetchState.FAILURE));
  isSuccess$ = this._workflowExecutionState.pipe(map(state => state === FetchState.SUCCESS));

  _outputs: BehaviorSubject<WorkflowVariable[]> = new BehaviorSubject([]);

  joinedOutput$ = this._outputs.pipe(map(outputs => outputs.map(o => o.properties.value).join('\n')));

  workflowId$: Observable<string>; 
  workflowConfig$: Observable<WorkflowStartConfig>;

  private readonly _destroyed: Subject<boolean> = new ReplaySubject(1);

  constructor(
    private workflows: WorkflowsService,
    private workflowInstances: WorkflowInstancesService,
    @Inject('$scope') private readonly $scope,
  ) { }

  ngOnInit(): void {
    const authorizationToken = JSON.parse(localStorage.getItem('ngStorage-Authorization') || '');
    this.workflows.defaultHeaders = this.workflows.defaultHeaders
      .set('Authorization', `Bearer ${authorizationToken}`);
    this.workflowInstances.defaultHeaders = this.workflowInstances.defaultHeaders
      .set('Authorization', `Bearer ${authorizationToken}`);

    this.workflowId$ = this.workflows.getWorkflowsList()
      .pipe(
        take(1),
        map((results) => results.find(item => item.unique_name === workflowUniqueName)),
        shareReplay(1),
        map(a => a?.id),
      );

    this.workflowConfig$ = this.workflowId$.pipe(
      mergeMap(
        (workflow: string | null) => iif(
          () => workflow != null,
          this.workflows.getWorkflowStartConfig(workflow).pipe(take(1)),
          throwError(() => new Error('Workflow not found')))
        ),
      ),
      shareReplay(1);
  }

  ngOnDestroy(): void {
    this._destroyed.next(true);
  }

  execWorkflow(): void {
    this._workflowExecutionState.next(FetchState.FETCHING);

    forkJoin([this.workflowConfig$, this.workflowId$])
      .pipe(
        map(([startConfig, id]) => {
          console.log('Remapping data')
          const formData = this.form.getFieldData();
          const input_variables = startConfig.input_variables.map(({ properties, ...data }) => ({
            ...data,
            properties: {
              ...properties,
              value: formData[properties.name],
            },
          }))
          return [ { ...startConfig, input_variables }, id  ] as [WorkflowStartConfig, string]
        }),
        mergeMap(([ config, id ]) => this.workflows.startWorkflow(id, config).pipe(take(1))),
        mergeMap(([ response ]) => this.getWorkflowInstance(response.id)),
        tap(_ => this._workflowExecutionState.next(FetchState.SUCCESS)),
        tap((instance: WorkflowInstance) => this._outputs.next(instance.variables.filter(v => v.properties.scope === 'output'))),
        catchError(err => {
          this._workflowExecutionState.next(FetchState.FAILURE); 
          return of(err);
        }),
        takeUntil(this._destroyed), 
      )
      .subscribe(); 
  }

  private getWorkflowInstance(id: string): Observable<WorkflowInstance> {
    return this.workflowInstances
      .getWorkflowInstance(id)
      .pipe(
        filter(instance => instance?.status?.state === 'success'),
        poll(10000)
      )
  }

  populateForm(initialValues: string[]): void {
    this.form = createHelloWorldForm(initialValues);
    this.$scope.$applyAsync();
    this.upload.open = false;
  }
}
