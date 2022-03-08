import { Component, Output, EventEmitter } from '@angular/core';
import template from './upload.component.html';
import './upload.component.scss';
import _ from 'lodash';

@Component({
  selector: 'wx-upload',
  host: {
    class: 'vms-standard-view wx-upload',
  },
  template
})
export class UploadComponent {

  @Output() public close: EventEmitter<any> = new EventEmitter<any>(true);
  fileToUpload: any = {};

  readClose(): void {
    if (!_.isEmpty(this.fileToUpload)) {
      const fileReader = new FileReader();
      fileReader.onloadend = () => {
        const rows = fileReader.result.toString().replace('\r', '').split('\n');
        this.close.emit(rows);
      }
      fileReader.readAsText(this.fileToUpload);
    } else {
      this.close.emit();
    }
  }
}
