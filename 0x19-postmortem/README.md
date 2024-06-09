# Postmortem Report

## Issue Summary
- **Duration**: June 7, 2024, 1:00 PM - June 7, 2024, 3:00 PM (UTC)
- **Impact**: The company's email notification system was down, preventing users from receiving important account notifications and alerts. Approximately 70% of users were affected.
- **Root Cause**: The outage was caused by an expired SSL certificate on the email server.

## Timeline
- **1:00 PM**: Issue detected when users started reporting that they were not receiving email notifications.
- **1:05 PM**: Monitoring alerts confirmed a failure in the email delivery system.
- **1:10 PM**: Engineers began investigating the email server logs to identify the cause of the failure.
- **1:20 PM**: Initial assumption was that the email service provider was experiencing issues.
- **1:30 PM**: Contacted the email service provider, who confirmed no issues on their end.
- **1:45 PM**: The issue was escalated to the DevOps team for further investigation.
- **2:00 PM**: DevOps team identified that the SSL certificate for the email server had expired.
- **2:15 PM**: Started the process to renew and install the new SSL certificate.
- **2:45 PM**: New SSL certificate installed successfully.
- **3:00 PM**: Email notification system functionality restored.

## Root Cause and Resolution
- **Root Cause**: The SSL certificate on the email server had expired, causing secure email delivery to fail.
- **Resolution**: The DevOps team renewed the SSL certificate and installed it on the email server, restoring secure email delivery.

## Corrective and Preventative Measures
- **Improvements**: Implement better certificate management practices and enhance monitoring for SSL certificate expiry.
- **Specific Tasks**:
  - Set up automated reminders for SSL certificate renewal well in advance of the expiry date.
  - Implement monitoring tools to alert the team about upcoming SSL certificate expirations.
  - Conduct regular audits of SSL certificates and their expiry dates.
  - Train the team on the importance of SSL certificates and how to manage them properly.
