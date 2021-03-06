import json

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_noop, ugettext_lazy as _


class Gig(models.Model):
    title = models.CharField(verbose_name=_("Gig name"),
                             max_length=60, blank=False)
    slug = models.SlugField(verbose_name=_("Slug"), blank=False)
    date = models.DateField(verbose_name=_("Gig date"), blank=False)
    description = models.TextField(verbose_name=_("Description"),
                                   null=False, blank=True)

    def __init__(self, *args, **kwargs):
        super(Gig, self).__init__(*args, **kwargs)
        self._pristine = {
            field.name: getattr(self, field.name)
            for field in self._meta.fields
        }

    def __str__(self):
        return "%s (%s)" % (self.title, self.date)

    def track_changes(self, user_making_changes):
        changes = []
        track_changes_of = [
            ('title', ugettext_noop('Gig name')),
            ('date', ugettext_noop('Gig date')),
            ('description', ugettext_noop('Description')),
        ]
        for field, verbose_name in track_changes_of:
            oldval = str(self._pristine[field] or '')
            newval = str(getattr(self, field))
            if oldval != newval:
                changes.append({
                    'title': verbose_name,
                    'title_translatable': True,
                    'prev': oldval,
                    'new': newval
                })
        if not changes:
            return
        action = (ugettext_noop('%(who)s (f) edited gig %(when)s')
                  if user_making_changes.profile.gender == 'f' else
                  ugettext_noop('%(who)s (m) edited gig %(when)s'))
        info = {'action': action, 'changes': changes}
        Comment.objects.create(
            gig=self, song=None, author=user_making_changes,
            text=json.dumps(info), comment_type=Comment.CT_GIG_EDIT,
        )


class CommentManager(models.Manager):
    def get_queryset(self):
        qs = super(CommentManager, self).get_queryset()
        return qs.select_related('song', 'author', 'gig')


class Comment(models.Model):
    objects = CommentManager()

    CT_SONG_COMMENT = 'song_comment'
    CT_SONG_EDIT = 'song_changed'
    CT_GIG_COMMENT = 'gig_comment'
    CT_GIG_EDIT = 'gig_changed'

    COMMENT_TYPE_CHOICES = (
        (CT_SONG_COMMENT, CT_SONG_COMMENT),
        (CT_GIG_COMMENT, CT_GIG_COMMENT),
        (CT_SONG_EDIT, CT_SONG_EDIT),
    )
    GIG_ONLY_COMMENTS = (CT_GIG_COMMENT, CT_GIG_EDIT)

    gig = models.ForeignKey(Gig, on_delete=models.CASCADE,
                            blank=False, related_name='comments')
    song = models.ForeignKey('sbsong.Song', on_delete=models.CASCADE,
                             blank=True, null=True, related_name='comments')
    comment_type = models.CharField(max_length=20, null=False, blank=False,
                                    choices=COMMENT_TYPE_CHOICES)
    author = models.ForeignKey(User, on_delete=models.PROTECT,
                               null=True, blank=True,
                               related_name='comments')
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField(null=False, blank=False)

    class Meta:
        ordering = ['-datetime']
        index_together = [
            ['author', 'datetime'],
            ['gig', 'datetime'],
            ['song', 'datetime'],
        ]
