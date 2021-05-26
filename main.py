from typing import Optional
from uuid import uuid4, UUID

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title='WikiRace', version='0.1.0')


class Page(BaseModel):
    name: str
    title: str


class GameLobby(BaseModel):
    start_page: Page
    end_page: Page
    id: Optional[UUID] = uuid4()
    pages: Optional[dict[str, Page]] = None


p1 = Page(name='Fort Stewart', title='Fort_Stewart')
p2 = Page(name='Pedhambe', title='Pedhambe')
p3 = Page(name='Lonnie Holley', title='Lonnie_Holley')
p4 = Page(name='Mark tree', title='Mark_tree')


fake_lobbies = [
    GameLobby(
        name='temp1',
        start_page=p1,
        end_page=p2,
        pages={
            p1.title: p1,
            p2.title: p2,
        }
    ),
    GameLobby(
        name='temp1',
        start_page=p3,
        end_page=p4,
        pages={
            p3.title: p3,
            p4.title: p4,
        }
    ),
]


@app.get('/')
def read_hello_world():
    return {'Hello': 'World'}


@app.get('/lobbies')
def read_lobbies():
    return fake_lobbies


@app.get('/lobbies/{lobby_id}')
def read_lobby(lobby_id: UUID):
    return fake_lobbies


@app.post('/lobbies', response_model=GameLobby)
def create_lobby(lobby: GameLobby):
    if lobby.pages is None:
        lobby.pages = {
            lobby.start_page.title: lobby.start_page,
            lobby.end_page.title: lobby.end_page,
        }
    return lobby
