from jmbo.models import ModelBase


class Video(ModelBase):
    content_id = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.content_id)
