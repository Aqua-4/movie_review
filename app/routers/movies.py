from fastapi import APIRouter

router = APIRouter()


@router.get("/movies/", tags=["movies"])
def read_movies():
    return [{"title": "Interstellar"}, {"title": "Inception"}]