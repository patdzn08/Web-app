FROM python
RUN pip install flask
COPY  ./static /home/myapp/static/
COPY  ./templates /home/myapp/templates/
COPY  design_app.py /home/myapp/
EXPOSE 5050
CMD python /home/myapp/design_app.py
