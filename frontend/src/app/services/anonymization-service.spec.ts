import { TestBed } from '@angular/core/testing';

import { AnonymizationService } from './anonymization-service';

describe('AnonymizationService', () => {
  let service: AnonymizationService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AnonymizationService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
