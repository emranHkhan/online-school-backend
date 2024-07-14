from rest_framework import generics
from comments.models import Comment
from comments.serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context
    
    def perform_create(self, serializer):
        serializer.save()

