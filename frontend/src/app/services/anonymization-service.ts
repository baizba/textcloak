import { Injectable } from '@angular/core';
import { AnonymizeRequest, AnonymizeResponse } from '../model/models';
import { Observable } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root',
})
export class AnonymizationService {
  private apiUrl: string = 'http://localhost:8000/anonymize';

  private headers = new HttpHeaders({
    'Content-Type': 'application/json',
  });

  constructor(private httpClient: HttpClient) {}

  anonymize(request: AnonymizeRequest): Observable<AnonymizeResponse> {
    return this.httpClient.post<AnonymizeResponse>(this.apiUrl, request, { headers: this.headers });
  }
}
