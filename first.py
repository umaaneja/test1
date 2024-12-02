I want to create a **multi-platform component diagram** for my system using Mermaid.js. Below are the details:

1. **System Overview**:
   - **System Name**: Multi-Platform E-Learning System
   - **Platforms**:
     - Web: For students and instructors to access via browsers.
     - Mobile: For students to use on smartphones.
     - Cloud: For data storage and API management.
   - **Technologies Used**:
     - Web: ReactJS, Node.js
     - Mobile: Flutter
     - Cloud: AWS, DynamoDB, Lambda functions

2. **Main Components**:
   - Web Platform:
     - User Dashboard: Displays course progress
     - Content Management: Allows instructors to upload material
   - Mobile Platform:
     - Mobile App: Provides course material and notifications
   - Cloud Platform:
     - API Gateway: Handles requests from web and mobile
     - Storage Service: Stores course material
     - Authentication Service: Manages user authentication
   - Shared/Universal Components:
     - Notification Service: Sends reminders across web and mobile

3. **Relationships Across Components**:
   - Within Web Platform:
     - User Dashboard interacts with Content Management to fetch updates.
   - Cross-Platform:
     - Mobile App interacts with API Gateway for course material.
     - API Gateway connects to Storage Service to retrieve data.

4. **Groups or Subsystems**:
   - Frontend: User Dashboard, Mobile App
   - Backend: API Gateway, Storage Service, Authentication Service

5. **Technology-Specific Details**:
   - The mobile app uses Flutter for cross-platform compatibility.
   - The API Gateway is deployed using AWS API Gateway.

6. **Style Preferences**:
   - Use blue for web components, green for mobile, and orange for cloud.
   - Add a note for the Authentication Service: "Uses OAuth2.0"

7. **Other Requirements**:
   - Include data flow arrows to show request/response paths.
   - Add a legend to explain color coding for platforms.
