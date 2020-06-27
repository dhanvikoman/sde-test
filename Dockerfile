FROM python:3

ADD my_script.py /

RUN pip install -r requirements.txt

CMD [ "python", "./sde-test-solution.py", "sample_input.json", "output_file.json" ]
