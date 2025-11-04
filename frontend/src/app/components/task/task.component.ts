import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { TaskService, Task } from '../../services/task.service';

@Component({
  selector: 'app-task',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './task.component.html',
  styleUrls: ['./task.component.css'],
})
export class TaskComponent implements OnInit {
  tasks: Task[] = [];
  newTask: string = '';

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks() {
    this.taskService.getTasks().subscribe((data) => {
      this.tasks = data;
    });
  }

  addTask() {
    if (this.newTask.trim()) {
      const task: Task = { title: this.newTask, completed: false };
      this.taskService.addTask(task).subscribe(() => {
        this.newTask = '';
        this.loadTasks();
      });
    }
  }

  toggleComplete(task: Task) {
    task.completed = !task.completed;
    this.taskService.updateTask(task).subscribe();
  }

  deleteTask(task: Task) {
    if (task.id) {
      this.taskService.deleteTask(task.id).subscribe(() => this.loadTasks());
    }
  }
}
