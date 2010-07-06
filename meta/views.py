# -*- coding: utf-8 -*-

from meta.models import *
from meta.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Main
def main_page(request):
    image_count = Image.objects.count()
    images = Image.objects.filter(highlight=True).order_by('?')
    image = images[0]
    thumbs = images.exclude(id=image.id)[:4]
    videos = Video.objects.filter(highlight=True).order_by('?')[:1]
    video = videos[0]
    tags = Tag.objects.all()
    locations = Sublocation.objects.exclude(name='')
    variables = RequestContext(request, {
        'image_count': image_count,
        'image': image,
        'thumbs': thumbs,
        'video': video,
        'tags': tags,
        'locations': locations,
        })
    return render_to_response('main_page.html', variables)

def search_page(request):
    form = SearchForm()
    query = ''
    images = []
    videos = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()
        if query:
            image_queryset = Image.objects.extra(
                    select={
                        'rank': "ts_rank_cd(tsv, plainto_tsquery('portuguese', %s), 32)",
                        },
                    where=["tsv @@ plainto_tsquery('portuguese', %s)"],
                    params=[query],
                    select_params=[query, query],
                    order_by=('-rank',)
                    )
            video_queryset = Video.objects.extra(
                    select={
                        'rank': "ts_rank_cd(tsv, plainto_tsquery('portuguese', %s), 32)",
                        },
                    where=["tsv @@ plainto_tsquery('portuguese', %s)"],
                    params=[query],
                    select_params=[query, query],
                    order_by=('-rank',)
                    )
            image_list = image_queryset
            video_list = video_queryset 
            images = get_paginated(request, image_list)
            videos = get_paginated(request, video_list)
            form = SearchForm({'query': query})
    variables = RequestContext(request, {
        'query': query,
        'form': form,
        'images': images,
        'videos': videos,
        'show_results': show_results,
        })
    return render_to_response('buscar.html', variables)

# Single
def image_page(request, image_id):
    image = get_object_or_404(Image, id=image_id)
    image.view_count = image.view_count + 1
    image.save()
    variables = RequestContext(request, {
        'media': image,
        'type': 'image',
        })
    return render_to_response('media_page.html', variables)

def video_page(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    video.view_count = video.view_count + 1
    video.save()
    variables = RequestContext(request, {
        'media': video,
        'type': 'video',
        })
    return render_to_response('media_page.html', variables)

def tag_page(request, tag_slug):
    images = []
    tag = get_object_or_404(Tag, slug=tag_slug)
    image_list = tag.images.order_by('-id')
    video_list = tag.videos.order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': tag,
        })
    return render_to_response('meta_page.html', variables)

    #if '&' and '|' in tag_name:
    #    and_tags = tag_name.split('&')
    #    for and_tag in and_tags:
    #        if '|' in and_tag:
    #            preor_imgs = []
    #            or_tags = and_tag.split('|')
    #            for or_tag in or_tags:
    #                or_tag = get_object_or_404(Tag, name=or_tag)
    #                or_imgs = or_tag.images.order_by('-id')
    #                preor_imgs.append(set(or_imgs))
    #            allor_imgs = preor_imgs[0]
    #            for or_set in preor_imgs:
    #                # Return union between sets
    #                allor_imgs |= or_set
    #            images.append(allor_imgs)
    #        else:
    #            and_tag = get_object_or_404(Tag, name=and_tag)
    #            and_imgs = and_tag.images.order_by('-id')
    #            images.append(set(and_imgs))
    #    final_set = images[0]
    #    for pre_set in images:
    #        # Return intersection between sets
    #        final_set &= pre_set
    #    images = final_set
    #elif '|' in tag_name:
    #    preor_imgs = []
    #    or_tags = tag_name.split('|')
    #    for or_tag in or_tags:
    #        or_tag = get_object_or_404(Tag, name=or_tag)
    #        or_imgs = or_tag.images.order_by('-id')
    #        preor_imgs.append(set(or_imgs))
    #    allor_imgs = preor_imgs[0]
    #    for or_set in preor_imgs:
    #        allor_imgs |= or_set
    #    images = allor_imgs
    #elif '&' in tag_name:
    #    and_tags = tag_name.split('&')
    #    for and_tag in and_tags:
    #        and_tag = get_object_or_404(Tag, name=and_tag)
    #        and_imgs = and_tag.images.order_by('-id')
    #        images.append(set(and_imgs))
    #    final_set = images[0]
    #    for pre_set in images:
    #        final_set &= pre_set
    #    images = final_set
    #else:
    #    tag = get_object_or_404(Tag, name=tag_name)
    #    images = tag.images.order_by('-id')

def author_page(request, author_slug):
    author = get_object_or_404(Author, slug=author_slug)
    image_list = Image.objects.filter(author__exact=author).order_by('-id')
    video_list = Video.objects.filter(author__exact=author).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': author,
        })
    return render_to_response('meta_page.html', variables)

def taxon_page(request, taxon_slug):
    taxon = get_object_or_404(Taxon, slug=taxon_slug)
    image_list = Image.objects.filter(taxon__exact=taxon).order_by('-id')
    video_list = Video.objects.filter(taxon__exact=taxon).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': taxon,
        })
    return render_to_response('meta_page.html', variables)

def genus_page(request, genus_slug):
    genus = get_object_or_404(Genus, slug=genus_slug)
    image_list = Image.objects.filter(genus__exact=genus).order_by('-id')
    video_list = Video.objects.filter(genus__exact=genus).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': genus,
        })
    return render_to_response('meta_page.html', variables)

def species_page(request, species_slug):
    species = get_object_or_404(Species, slug=species_slug)
    image_list = Image.objects.filter(species__exact=species).order_by('-id')
    video_list = Video.objects.filter(species__exact=species).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': species,
        })
    return render_to_response('meta_page.html', variables)

def size_page(request, size_slug):
    size = get_object_or_404(Size, slug=size_slug)
    image_list = Image.objects.filter(size__exact=size).order_by('-id')
    video_list = Video.objects.filter(size__exact=size).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': size,
        })
    return render_to_response('meta_page.html', variables)

def sublocation_page(request, sublocation_slug):
    sublocation = get_object_or_404(Sublocation, slug=sublocation_slug)
    image_list = Image.objects.filter(sublocation__exact=sublocation).order_by('-id')
    video_list = Video.objects.filter(sublocation__exact=sublocation).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': sublocation,
        })
    return render_to_response('meta_page.html', variables)

def city_page(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    image_list = Image.objects.filter(city__exact=city).order_by('-id')
    video_list = Video.objects.filter(city__exact=city).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': city,
        })
    return render_to_response('meta_page.html', variables)

def state_page(request, state_slug):
    state = get_object_or_404(State, slug=state_slug)
    image_list = Image.objects.filter(state__exact=state).order_by('-id')
    video_list = Video.objects.filter(state__exact=state).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': state,
        })
    return render_to_response('meta_page.html', variables)

def country_page(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    image_list = Image.objects.filter(country__exact=country).order_by('-id')
    video_list = Video.objects.filter(country__exact=country).order_by('-id')
    images = get_paginated(request, image_list)
    videos = get_paginated(request, video_list)
    variables = RequestContext(request, {
        'images': images,
        'videos': videos,
        'meta': country,
        })
    return render_to_response('meta_page.html', variables)

# Lists
def tag_list_page(request):
    tags = Tag.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': tags,
        'plural': u'Marcadores',
        'url': 'tag',
        })
    return render_to_response('meta_list_page.html', variables)

def author_list_page(request):
    authors = Author.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': authors,
        'plural': u'Autores',
        'url': 'autor'
        })
    return render_to_response('meta_list_page.html', variables)

def taxon_list_page(request):
    taxa = Taxon.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': taxa,
        'plural': u'Táxons',
        'url': 'taxon',
        })
    return render_to_response('meta_list_page.html', variables)

def genus_list_page(request):
    genera = Genus.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': genera,
        'plural': u'Gêneros',
        'url': 'genero',
        })
    return render_to_response('meta_list_page.html', variables)

def species_list_page(request):
    spp = Species.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': spp,
        'plural': u'Espécies',
        'url': 'especie',
        })
    return render_to_response('meta_list_page.html', variables)

def size_list_page(request):
    sizes = Size.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': sizes,
        'plural': u'Tamanhos',
        'url': 'tamanho',
        })
    return render_to_response('meta_list_page.html', variables)

def sublocation_list_page(request):
    sublocations = Sublocation.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': sublocations,
        'plural': u'Locais',
        'url': 'local',
        })
    return render_to_response('meta_list_page.html', variables)

def city_list_page(request):
    cities = City.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': cities,
        'plural': u'Cidades',
        'url': 'cidade',
        })
    return render_to_response('meta_list_page.html', variables)

def state_list_page(request):
    states = State.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': states,
        'plural': u'Estados',
        'url': 'estado',
        })
    return render_to_response('meta_list_page.html', variables)

def country_list_page(request):
    countries = Country.objects.order_by('name')
    variables = RequestContext(request, {
        'metas': countries,
        'plural': u'Países',
        'url': 'pais',
        })
    return render_to_response('meta_list_page.html', variables)

# Menu
def taxa_page(request):
    genera = Genus.objects.order_by('name')
    variables = RequestContext(request, {
        'genera': genera,
        })
    return render_to_response('taxa_page.html', variables)

def places_page(request):
    sublocations = Sublocation.objects.exclude(name='').order_by('name')
    cities = City.objects.exclude(name='').order_by('name')
    states = State.objects.exclude(name='').order_by('name')
    countries = Country.objects.exclude(name='').order_by('name')
    variables = RequestContext(request, {
        'sublocations': sublocations,
        'cities': cities,
        'states': states,
        'countries': countries,
        })
    return render_to_response('places_page.html', variables)

def tags_page(request):
    tags = Tag.objects.exclude(name='').order_by('parent')
    sizes = Size.objects.exclude(name='').order_by('id')
    variables = RequestContext(request, {
        'tags': tags,
        'sizes': sizes,
        })
    return render_to_response('tags_page.html', variables)

# Internal functions
def get_paginated(request, obj_list):
    paginator = Paginator(obj_list, 16)
    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    # If page request (9999) is out of range, deliver last page of results.
    try:
        obj = paginator.page(page)
    except (EmptyPage, InvalidPage):
        obj = paginator.page(paginator.num_pages)
    return obj