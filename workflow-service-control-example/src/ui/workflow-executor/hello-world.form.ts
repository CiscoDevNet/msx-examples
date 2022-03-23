import { Form } from '@cisco-msx/forms';
import { requiredValidator } from '@cisco-msx/forms/validators';
import _ from 'lodash';
export function createHelloWorldForm(initialValues?: string[]): Form {
  const form = new Form();
  form.setFields([
    {
      name: 'Input1',
      type: 'input',
      initialValue: _.get(initialValues, '[0]', ''),
      validators: [requiredValidator],
      properties: {
        required: true,
        label: 'Input1',
      },
    },
    {
      name: 'Input2',
      type: 'input',
      initialValue: _.get(initialValues, '[1]', ''),
      validators: [requiredValidator],
      properties: {
        required: true,
        label: 'Input2',
      },
    },
  ]);
  return form;
}
