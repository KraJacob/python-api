
#Création de l'appi dans le cadre du Bootcamp
from flask_restplus import fields
from controllers.restplus import api


personnel_post = api.model('personnel post', {
    "id_pers": fields.String(required=True, description='The unique identifier of personnel'),
    "name": fields.String(required=True, description='The personnel name'),
    "firstname": fields.String(required=True, description='The personnel firstname'),
    "birthday": fields.String(required=True, description='The personnel birthday'),
    "role": fields.String(required=True, description='The personnel role'),
    "id_startup": fields.String(required=True, description='the startup id')

    })

personnel_get = api.model('personnel get', {
    "id_pers": fields.String(readOnly=True, description='The unique identifier of personnel'),
    "name": fields.String(required=True, description='The personnel name'),
    "firstname": fields.String(required=True, description='The personnel firstname'),
    "birthday": fields.String(required=True, description='The personnel birthday'),
    "role": fields.String(required=True, description='The personnel role'),
    "id_startup": fields.String(required=True, description='the startup id')

    })

personnel_put = api.model('personnel put', {
    "id_pers": fields.String(required=True, description='The unique identifier of personnel'),
    "name": fields.String(required=True, description='The personnel name'),
    "firstname": fields.String(required=True, description='The personnel firstname'),
    "birthday": fields.String(required=True, description='The personnel birthday'),
    "role": fields.String(required=True, description='The personnel role'),
    "id_startup": fields.String(required=True, description='the startup id')

    })


startup_post = api.model('Recipe post', {
    "startup_name": fields.String(required=True, description='name of startup'),
    "post_date": fields.String(required=True, description='Date post'),
    "social_network": fields.String(required=True, description='Social Network'),
    "url_on_social_network": fields.String(required=True, description='URL social network'),
    "post_url": fields.String(required=True, description='The URL of post'),
    "post_autor": fields.String(required=True, description='The post autor'),
    "post_contenu": fields.String(required=True, description='The post contenu'),
    "nbr_like": fields.Integer(required=True, description='The nbr like '),
    "nbr_dislike": fields.Integer(required=True, description='The he nbr dislike'),
    "nbr_share": fields.Integer(required=True, description='The nbr share'),
    "tags": fields.List(fields.String,required=True, description='The tags')
})

startup_get = api.model('Recipe get', {
    "startup_name": fields.String(required=True, description='name of startup'),
    "post_date": fields.String(required=True, description='Date post'),
    "social_network": fields.String(required=True, description='Social Network'),
    "url_on_social_network": fields.String(required=True, description='URL social network'),
    "post_url": fields.String(required=True, description='The URL of post'),
    "post_autor": fields.String(required=True, description='The post autor'),
    "post_contenu": fields.String(required=True, description='The post contenu'),
    "nbr_like": fields.Integer(required=True, description='The nbr like '),
    "nbr_dislike": fields.Integer(required=True, description='The he nbr dislike'),
    "nbr_share": fields.Integer(required=True, description='The nbr share'),
    "tags": fields.List(fields.String,required=True, description='The tags')
})

comment_post = api.model('Comment post', {
    "autor": fields.String(required=True, description='The autor name'),
    "date": fields.Date(required=True, description='The date of publication'),
    "idpublication": fields.Integer(required=True, description='Id publication'),
    "contenu": fields.String(required=True, description='The cooking time'),
    "idstartup": fields.String(required=True, description='The total duration'),
    "tag_list": fields.List(fields.String,required=True, description='The recipe ingredients list'),
    "like": fields.Integer(required=True, description='The recipe ingredients list'),
    "dislike": fields.Integer(required=True, description='The recipe ingredients list'),
 })

comment_get = api.model('Comment get', {
    "autor": fields.String(required=True, description='The autor name'),
    "date": fields.Date(required=True, description='The date of publication'),
    "idpublication": fields.String(required=True, description='Id publication'),
    "contenu": fields.String(required=True, description='The cooking time'),
    "idstartup": fields.String(required=True, description='The total duration'),
    "tag_list": fields.List(fields.String, required=True, description='The recipe ingredients list'),
    "like": fields.Integer(required=True, description='The recipe ingredients list'),
    "dislike": fields.Integer(required=True, description='The recipe ingredients list'),

})

comment_delete = api.model('Comment delete', {
    "autor": fields.String(required=True, description='The autor name'),
    "date": fields.Date(required=True, description='The date of publication'),
    "idpublication": fields.String(required=True, description='Id publication'),
    "contenu": fields.String(required=True, description='The cooking time'),
    "idstartup": fields.String(required=True, description='The total duration'),
    "tag_list": fields.List(fields.String, required=True, description='The recipe ingredients list'),
    "like": fields.Integer(required=True, description='The recipe ingredients list'),
    "dislike": fields.Integer(required=True, description='The recipe ingredients list'),
})

comment_update = api.model('Comment update', {
    "autor": fields.String(required=True, description='The autor name'),
    "date": fields.Date(required=True, description='The date of publication'),
    "idpublication": fields.String(required=True, description='Id publication'),
    "contenu": fields.String(required=True, description='The cooking time'),
    "idstartup": fields.String(required=True, description='The total duration'),
    "tag_list": fields.List(fields.String, required=True, description='The recipe ingredients list'),
    "like": fields.Integer(required=True, description='The recipe ingredients list'),
    "dislike": fields.Integer(required=True, description='The recipe ingredients list'),
})

