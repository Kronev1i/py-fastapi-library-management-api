from typing import List

from models import Author, Book
from schemas import AuthorCreate, BookCreate
from sqlalchemy.orm import Session


def get_author(
        db: Session,
        author_id: int
):
    return db.query(Author).filter(Author.id == author_id).first()

def get_authors(
        db: Session,
        skip: int = 0, 
        limit: int = 10
):
  return db.offset(skip).limit(limit).all()

def create_author(
        db: Session,
        author: AuthorCreate
) -> Author:
    db_author = Author(name=author.name, bio=author.bio)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_books(
        db: Session,
        skip: int = 0,
        limit: int = 10,
        author_id: int | None = None
):
  query = db.query(Book)
  if author_id is not None:
    query = query.filter(Book.author_id == author_id)
  return query.offset(skip).limit(limit).all()

def create_book(db: Session, book: BookCreate) -> Book:
    db_book = Book(
        title=book.title,
        summary=book.summary,
        author_id=book.author_id,
        publication_date=book.publication_date,
        author=book.author_id,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

