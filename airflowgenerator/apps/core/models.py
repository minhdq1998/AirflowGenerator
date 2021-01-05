from abc import abstractmethod

from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255, null=True)
    task_id = models.CharField(max_length=255, null=False, unique=True)

    @abstractmethod
    def to_code(self, trailing = ''):
        return """"""

class DummyTask(Task):
    """
    Model represent DummyTask definition
    """

    def to_code(self, trailing = ''):
        return f"""{trailing}{self.name} = DummyOperator(task_id='{self.task_id}', dag=dag)"""

class S3ToGoogleCloudStorageTask(Task):
    """
    Model represent S3ToGoogleCloudStorageOperator definition
    """
    bucket = models.CharField(max_length=255, null=False)
    prefix = models.TextField(max_length=255, null=False)
    delimiter = models.TextField(max_length=255, null = False)
    dest_gcs_conn_id = models.CharField(max_length=255, null=False)
    dest_gcs = models.TextField(max_length=255, null=False)
    replace = models.BooleanField(max_length=255, default=True)

    def to_code(self, trailing = ''):
        return f"""
        {trailing}{self.name} = S3ToGoogleCloudStorageOperator(
        {trailing}  task_id='{self.task_id}',
        {trailing}  bucket='{self.bucket}',
        {trailing}  prefix='{self.prefix}',
        {trailing}  dest_gcs_conn_id='{self.dest_gcs_conn_id}',
        {trailing}  dest_gcs='{self.dest_gcs}',
        {trailing}  replace={self.replace},
        {trailing}  dag=my-dag
        )
        """

DAG_TEMPLATE = """
import pendulum


"""


class DagFile(models.Model):
    """
    Models represent the DAG definition file
    """
    # Fields for DAG object create
    name = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, default='No Description')
    schedule_interval=models.CharField(max_length=255, default = '')
    start_date=models.CharField(max_length=255, default = '')
    #===============================

    # Fields for default_args object create
    owner = models.CharField(max_length=255, default='airflow')
    depend_on_past = models.BooleanField(default=True)
    email_on_failure = models.BooleanField(default=False)
    retries = models.SmallIntegerField(default=0)
    retry_delay = models.SmallIntegerField(default=5)
    tasks = models.ManyToManyField(Task, blank=True)
    #===============================

    def to_code(self, trailing = ''):
        return DAG_TEMPLATE
    

