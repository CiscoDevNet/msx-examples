class WorkspaceHooks {
	getServiceControlsConfig() {
		return {
			label: 'workflowexecutor.service.property.name',
			description: 'workflowexecutor.service.service.controls.description',
			controls: [
				{
					label: 'workflowexecutor.service_control.workflow_executor.name',
					iconClass: 'vms_fi_editor7040-24',
					description: 'workflowexecutor.service_control.workflow_executor.description',
					route: 'app.workflow-executor'
				}
			],
		};
	}
}

export { WorkspaceHooks as hooksClass };
