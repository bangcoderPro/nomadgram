from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class Notifications(APIView):

    def get(self, request, format=None):

        user = request.user

        notifications = models.Notification.objects.filter(to=user)

        serializer = serializers.NotificationSerializer(notifications, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

def create_notification(creator, to, notification_type, image=None, comment=None):

    print(creator, to, notification_type, image, comment  )

    notification = models.Notification.objects.create(
        creator=creator,
        to=to,
        notification_type=notification_type,
        image=image,
        comment=comment,
    )

    notification.save()





# class Feed(APIView):

#     def get(self, request, format=None):

#         user=request.user

#         following_users = user.following.all()

#         image_list = []

#         for following_user in following_users:

#             user_images = following_user.images.all()[:2]

#             for image in user_images:

#                 image_list.append(image)

#         sorted_list = sorted(image_list, key=lambda image: image.created_at, reverse=True)

#         serializer = serializers.ImageSerializer(sorted_list, many=True)

#         return Response(serializer.data)