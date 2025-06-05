"""
채팅방별 websocket 연결을 관리하는 싱글턴
"""
from typing import Dict, Set
from fastapi import WebSocket

class ChatManager:
    def __init__(self):
        self.active_rooms: Dict[int, Set[WebSocket]] = {}

    # --- connection 관리 ---
    async def connect(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        self.active_rooms.setdefault(room_id, set()).add(websocket)

    def disconnect(self, websocket: WebSocket, room_id: int):
        self.active_rooms.get(room_id, set()).discard(websocket)

    # --- 메시지 브로드캐스트 ---
    async def broadcast(self, room_id: int, data: dict):
        for ws in list(self.active_rooms.get(room_id, set())):
            try:
                await ws.send_json(data)
            except Exception:
                self.disconnect(ws, room_id)

    def is_user_online(self, room_id: int, user_id: int) -> bool:
        # user_id → 웹소켓 매핑을 별도로 유지하려면 확장
        return bool(self.active_rooms.get(room_id))
        
chat_manager = ChatManager()
