from csv import DictReader

from django.core.management import BaseCommand
# from reviews.models import (Category, Comment, Genre, Review,
#                             Title, User)
from reviews.models import Comment, Review
from users.models import User
from titles.models import Category, Genre, Title


class User(BaseCommand):
    help = 'Loads user.csv data'

    def handle(self, *args, **options):
        for row in DictReader(
            open('./static/data/user.csv')
        ):
            user = User(
                id=row['id'], username=row['username'],
                email=row['email'], role=row['role'],
                bio=row['bio'], first_name=row['first_name'],
                last_name=row['last_name']
            )
            user.save()


class Category(BaseCommand):
    help = 'Loads category.csv data'

    def handle(self, *args, **options):
        for row in DictReader(
            open('./static/data/category.csv')
        ):
            category = Category(
                id=row['id'], name=row['name'], slug=row['slug']
            )
            category.save()


class Genre(BaseCommand):
    help = 'Loads genre.csv data'

    def handle(self, *args, **options):
        for row in DictReader(
            open('./static/data/genre.csv')
        ):
            genre = Genre(id=row['id'], name=row['name'], slug=row['slug'])
            genre.save()


class Review(BaseCommand):
    help = 'Loads review.csv data'

    def handle(self, *args, **options):
        for row in DictReader(
            open('./static/data/review.csv')
        ):
            review = Review(
                id=row['id'], title_id=row['title_id'],
                text=row['text'], author=row['author'],
                score=row['score'], pub_date=row['pub_date']
            )
            review.save()


class Title(BaseCommand):
    help = 'Loads title.csv data'

    def handle(self, *args, **options):
        for row in DictReader(
            open('./static/data/titles.csv')
        ):
            title = Title(
                id=row['id'], name=row['name'],
                year=row['year'], category_id=row['category']
            )
            title.save()


class Comment(BaseCommand):
    help = 'Loads comment.csv data'

    def handle(self, *args, **options):
        for row in DictReader(
            open('./static/data/comment.csv')
        ):
            comment = Comment(
                id=row['id'], review_id=row['review_id'],
                text=row['text'], author=row['author'],
                pub_date=row['pub_date']
            )
            comment.save()
