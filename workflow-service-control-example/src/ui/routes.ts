import type { Ng2StateDeclaration } from '@uirouter/angular';

export const routes: Ng2StateDeclaration[] = [
  {
    name: 'app.workflow-executor.**',
    url: '/workflow-executor',
    loadChildren: () =>
      import('./workflow-executor').then(mod => mod.WorkflowExecutorModule),
  },
];
