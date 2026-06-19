import {Component, signal} from '@angular/core';
import {FormsModule} from '@angular/forms';

@Component({
  selector: 'app-root',
  imports: [FormsModule],
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class App {
  inputText = '';
  outputText = '';

  anonymize(): void {
    if (!this.inputText || this.inputText.trim().length === 0) {
      return;
    }

    this.outputText = this.inputText;
    alert('Demo mode: Real anonymization backend coming soon!');
  }

  isCopyDisabled(): boolean {
    return !this.outputText || this.outputText.trim().length === 0;
  }

  protected copyText() {
    if (this.isCopyDisabled()) {
      return;
    }
    navigator.clipboard.writeText(this.outputText);
  }
}
