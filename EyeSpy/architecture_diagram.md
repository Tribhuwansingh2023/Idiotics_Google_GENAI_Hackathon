# EyeSpy System Diagrams

## 1. System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        FRONTEND LAYER                          │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │   Text Input    │    │  Image Upload   │                    │
│  │   Text Area     │    │   File Input    │                    │
│  └─────────────────┘    └─────────────────┘                    │
│           │                       │                             │
│           └───────────┬───────────┘                             │
│                       │                                         │
│              ┌─────────────────┐                               │
│              │ JavaScript API  │                               │
│              │   fetch() calls │                               │
│              └─────────────────┘                               │
└─────────────────────────┼───────────────────────────────────────┘
                          │ HTTP/REST API
                          │ (JSON/FormData)
┌─────────────────────────▼───────────────────────────────────────┐
│                    APPLICATION LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │                 Flask Routes                                │ │
│  │  POST /api/analyze-text    POST /api/analyze-image         │ │
│  │  GET  /api/health                                          │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                    BUSINESS LOGIC LAYER                       │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────────────────┐ │
│  │              FakeNewsDetector Class                         │ │
│  │                                                             │ │
│  │  ┌─────────────────┐  ┌─────────────────┐                  │ │
│  │  │  Text Analysis  │  │ Image Analysis  │                  │ │
│  │  │     Engine      │  │     Engine      │                  │ │
│  │  └─────────────────┘  └─────────────────┘                  │ │
│  └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────┬───────────────────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────────────────┐
│                    DATA/MODEL LAYER                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌─────────────────┐    ┌─────────────────┐                    │
│  │  TF-IDF         │    │  Logistic       │                    │
│  │  Vectorizer     │    │  Regression     │                    │
│  │  (vectorizer.pkl)│    │  (model.pkl)    │                    │
│  └─────────────────┘    └─────────────────┘                    │
└─────────────────────────────────────────────────────────────────┘

```

## 2. Use Case Diagram

```
                    ┌─────────────────┐
                    │      User       │
                    └─────────┬───────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
    ┌─────────────────┐ ┌─────────────┐ ┌─────────────┐
    │  Upload Image   │ │ Enter Text  │ │View Results │
    │   for Analysis  │ │for Analysis │ │& Confidence │
    └─────────────────┘ └─────────────┘ └─────────────┘
              │               │               ▲
              │               │               │
              └───────────────┼───────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │   EyeSpy System │
                    └─────────┬───────┘
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
    ┌─────────────────┐ ┌─────────────┐ ┌─────────────┐
    │Analyze Image    │ │Analyze Text │ │Generate     │
    │Manipulation     │ │for Fake News│ │Confidence   │
    └─────────────────┘ └─────────────┘ │Score        │
              │               │         └─────────────┘
              │               │               ▲
              └───────────────┼───────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │ML/Rule Engine   │
                    └─────────────────┘
```

## 3. Data Flow Diagram

```
[User] ──(1)──> [Frontend] ──(2)──> [Flask API] ──(3)──> [FakeNewsDetector]
   ▲                                                              │
   │                                                              ▼
   │                                                    [ML Models & Rules]
   │                                                              │
   │                                                              ▼
   └──(6)── [Result Display] <──(5)── [JSON Response] <──(4)── [Analysis]

Flow Steps:
1. User inputs text/image
2. Frontend sends HTTP request
3. API routes to detector
4. ML analysis & rule checking
5. JSON response with confidence
6. UI displays results
```

## 4. Component Interaction Flow

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Frontend   │    │   Backend   │    │ ML Engine   │
│             │    │             │    │             │
│ ┌─────────┐ │    │ ┌─────────┐ │    │ ┌─────────┐ │
│ │Text/Img │ │───▶│ │Flask API│ │───▶│ │TF-IDF   │ │
│ │ Input   │ │    │ │Routes   │ │    │ │Vector   │ │
│ └─────────┘ │    │ └─────────┘ │    │ └─────────┘ │
│             │    │             │    │             │
│ ┌─────────┐ │    │ ┌─────────┐ │    │ ┌─────────┐ │
│ │Results  │ │◀───│ │Response │ │◀───│ │LogReg   │ │
│ │Display  │ │    │ │Handler  │ │    │ │Model    │ │
│ └─────────┘ │    │ └─────────┘ │    │ └─────────┘ │
└─────────────┘    └─────────────┘    └─────────────┘
```

## Key Components:

- **Frontend**: Responsive UI with file upload and text input
- **API Layer**: RESTful endpoints with CORS support  
- **ML Engine**: TF-IDF vectorization + Logistic Regression
- **Rule Engine**: Pattern matching for fake news indicators
- **Scoring System**: Combined confidence metrics
```