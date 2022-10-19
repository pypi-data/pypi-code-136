
from sdm.core.jobs import job_service
from sdm.examples.jobs import HelloWorld

job_service._jobs["HelloWorld"] = HelloWorld

people = ["Nico", "Gabriel", "Emilio", "Fernan"]

job = job_service.create("HelloWorld")
job.prepare()
for p in people:
    job.submit(p)
job.done()

