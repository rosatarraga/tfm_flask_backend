import { Component } from "@angular/core";
import { MatDialogRef } from "@angular/material/dialog";

@Component({
    selector: 'dialog',
    templateUrl: './dialog.html',
  })
  export class Dialog {
    constructor(public dialogRef: MatDialogRef<Dialog>) {}
  } 