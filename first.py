graph TD
    %% Style Definitions
    classDef web fill:#cce5ff,stroke:#003399,stroke-width:2px; %% Blue for Web
    classDef mobile fill:#d4edda,stroke:#006600,stroke-width:2px; %% Green for Mobile
    classDef cloud fill:#ffeeba,stroke:#996600,stroke-width:2px; %% Orange for Cloud
    classDef shared fill:#f8d7da,stroke:#990000,stroke-width:2px; %% Red for Shared/Universal Components

    %% Web Platform Components
    WD[User Dashboard]:::web
    CM[Content Management]:::web
    
    %% Mobile Platform Components
    MA[Mobile App]:::mobile

    %% Cloud Platform Components
    API[a Gateway]:::cloud
    SS[Storage Service]:::cloud
    AS[Authentication Service]:::cloud

    %% Shared/Universal Components
    NS[Notification Service]:::shared

    %% Relationships
    WD --> CM
    MA --> API
    API --> SS
    API --> AS
    NS --> WD
    NS --> MA

    %% Grouping
    subgraph Frontend [Frontend]
        WD
        MA
    end

    subgraph Backend [Backend]
        API
        SS
        AS
    end
