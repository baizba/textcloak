import { Component, inject, signal } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatSnackBar } from '@angular/material/snack-bar';
import { AnonymizationService } from './services/anonymization-service';
import { AnonymizeRequest } from './model/models';

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App {
  inputText = signal('');
  outputText = signal('');

  private snackBar = inject(MatSnackBar);
  private anonymizationService = inject(AnonymizationService);

  anonymize(): void {
    const text = this.inputText();
    if (!text || text.trim().length === 0) {
      return;
    }

    const request: AnonymizeRequest = { text };

    this.anonymizationService.anonymize(request).subscribe({
      next: (response) => {
        this.outputText.set(response.anonymizedText);
      },
      error: (error) => {
        console.error('Anonymization failed:', error);
        this.snackBar.open('Anonymization failed!', 'Dismiss', { duration: 1000 });
      },
    });
  }

  isCopyDisabled(): boolean {
    const text = this.outputText();
    return !text || text.trim().length === 0;
  }

  protected copyText() {
    if (this.isCopyDisabled()) {
      return;
    }
    navigator.clipboard.writeText(this.outputText());
    this.snackBar.open('Text copied!', 'Dismiss', { duration: 1000 });
  }
}
