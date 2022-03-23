import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';
import { BASE_PATH, MsxApiModule } from '@cisco-msx/angular-api-client';
import { MsxCommonModule } from '@cisco-msx/common';
import { MsxFormsModule } from '@cisco-msx/forms';
import { UploadComponent } from './upload.component';

@NgModule({
  imports: [
    CommonModule,
    MsxCommonModule,
    MsxFormsModule,
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
    UploadComponent,
  ],
  entryComponents: [
    UploadComponent,
  ],
  exports: [
    UploadComponent
  ]
})
export class UploadModule {
}
