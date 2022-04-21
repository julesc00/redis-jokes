# Dango app with Channels, Redis and Celery

### Description  
The app receives some jokes from an api, and uses Celery Beat scheduler and worker to asynchronously get and provide
the text to the template.  
Used docker containers.