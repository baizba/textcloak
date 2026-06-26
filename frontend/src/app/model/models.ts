export interface AnonymizeRequest {
  text: string;
}

export interface ReplacementItem {
  start: number;
  end: number;
  replacementText: string;
}

export interface AnonymizeResponse {
  anonymizedText: string;
  replacementItems: ReplacementItem[];
}
