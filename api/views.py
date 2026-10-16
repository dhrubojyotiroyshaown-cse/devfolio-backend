
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import (
    Profile,
    Skill,
    Experience,
    Education,
    Project,
    Category,
    Tag,
    Post,
    ContactMessage,
)

from .serializers import (
    ProfileSerializer,
    SkillSerializer,
    ExperienceSerializer,
    EducationSerializer,
    ProjectSerializer,
    CategorySerializer,
    TagSerializer,
    PostSerializer,
    ContactMessageSerializer,
)

from .permissions import IsAdminOrReadOnly


# Profile API
class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self):
        return Profile.objects.first()


# Skills API
class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["category"]
    search_fields = ["name"]
    ordering_fields = ["name", "display_order"]


# Experience API
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    permission_classes = [AllowAny]


# Education API
class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
    permission_classes = [AllowAny]


# Public Project List API
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "title"]


# Public Project Details API
class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"


# Create Project API
class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]


# Retrieve, Update, or Delete Project API
class ProjectManageView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = "slug"


# Categories API
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


# Tags API
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


# Published Blog Posts API
class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    filterset_fields = ["category__slug", "tags__slug"]
    search_fields = ["title", "excerpt", "content"]
    ordering_fields = ["published_at", "created_at", "views"]

    def get_queryset(self):
        return Post.objects.filter(status="published")


# Published Blog Details API
class PostDetailView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"

    def get_queryset(self):
        return Post.objects.filter(status="published")


# Contact Message API
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    permission_classes = [AllowAny]
