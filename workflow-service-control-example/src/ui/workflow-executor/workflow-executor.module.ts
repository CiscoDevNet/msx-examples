import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { BASE_PATH, MsxApiModule } from '@cisco-msx/angular-api-client';
import { MsxCommonModule } from '@cisco-msx/common';
import { MsxFormsModule } from '@cisco-msx/forms';
import { UIRouterModule } from '@uirouter/angular';
import { WorkflowExecutorComponent } from './workflow-executor.component';
import { UploadModule } from '../upload/upload.module';

@NgModule({
  imports: [
    CommonModule,
    MsxCommonModule,
    MsxFormsModule,
    UploadModule,
    UIRouterModule.forChild({
      states: [
        {
          name: 'app.workflow-executor',
          url: '/workflow-executor',
          views: {
            'module@app': {
              component: WorkflowExecutorComponent
            }
          },
        },
      ]
    }),
    HttpClientModule,
    MsxApiModule,
  ],
  providers: [
    {
      provide: BASE_PATH,
      useFactory: () =>
        JSON.parse(localStorage.getItem('ngStorage-API_GATEWAY_HOSTNAME') || '')
    },
  ],
  declarations: [
    WorkflowExecutorComponent
  ],
  entryComponents: [
    WorkflowExecutorComponent
  ]
})
export class WorkflowExecutorModule {
}
