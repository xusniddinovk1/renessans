from modeltranslation.translator import register, TranslationOptions
from .models import Activity, Hotel, Education, RecreationZone, News

@register(Activity)
class ActivityTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('name', 'description')

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(RecreationZone)
class RecreationZoneTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
