# Plugins


PLUGINS = [
    'pelican.plugins.webassets',
    # 'pelican.plugins.i18n_subsites',
    'pelican_vimeo',
]

WEBASSETS_BUNDLES = [
    (
        'stylesheets',
        ['css/base.css'],
        {'output': 'css/style.min.css', 'filters': ['root_postcss']}
    ),
]


# Site information

AUTHOR = "A+A"

SITENAME = "SBAU 2021"

SITEDESCRIPTION = "Seoul Biennale of Architecture & Urbanism, 2021"


# URLs

SITEURL = ''

# Uncomment for document-relative URLs when developing
# RELATIVE_URLS = True


# I18n

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

LANGUAGES = {
    'ko': "Korean",
    'en': "English"
}

# Uncomment for document-relative URLs
#RELATIVE_URLS = True


# Content generation

PATH = 'content/'

STATIC_PATHS = ['images']

THEME = 'theme/'

DEFAULT_PAGINATION = False

INDEX_SAVE_AS = ''
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '/' + PAGE_SAVE_AS
PAGE_LANG_SAVE_AS = '{lang}/{slug}.html'
PAGE_LANG_URL = '/' + PAGE_LANG_SAVE_AS
PAGES_SAVE_AS = ''
TAGS_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''


# Feed generation

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


