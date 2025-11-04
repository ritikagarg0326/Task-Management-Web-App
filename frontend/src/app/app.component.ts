import { Component } from '@angular/core';
import { TaskComponent } from './components/task/task.component';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TaskComponent, HttpClientModule],
  template: `<app-task></app-task>`,
})
export class AppComponent {}
