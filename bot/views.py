from typing import Any

from rest_framework import generics, permissions
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request
from rest_framework.response import Response

from bot.models import TgUser
from bot.serializers import TgUserSerializer
from bot.tg.client import TgClient


class VerificationView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TgUserSerializer

    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        serializer: TgUserSerializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tg_user: TgUser = serializer.save(user=request.user)

        try:
            tg_user = TgUser.objects.get(verification_code=serializer.validated_data["verification_code"])
        except TgUser.DoesNotExist:
            raise AuthenticationFailed

        tg_user.user = request.user
        tg_user.save()

        TgClient().send_message(tg_user.chat_id, 'Bot token verified')

        return Response(TgUserSerializer(tg_user).data)
