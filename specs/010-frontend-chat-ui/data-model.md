# Data Model – Feature 010: Frontend Chat UI

## Frontend Message Model

```ts
type Role = 'user' | 'assistant';

interface Citation {
  path: string;
  chapter: string;
  section?: string | null;
  score?: number | null;
}

interface Message {
  id: string;
  role: Role;
  content: string;
  citations?: Citation[];
}
```

## Backend ChatResponse

```ts
interface ChatResponse {
  answer: string;
  citations: Citation[];
  stream: boolean;
}
```


