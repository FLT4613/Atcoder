FROM python:3-alpine
RUN apk --no-cache add gcc libc-dev libxml2-dev libxslt-dev
RUN pip install requests pyquery
WORKDIR /root/
CMD ["python", "/root/collect.py"]