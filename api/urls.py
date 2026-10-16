from django.urls import path

from .views import (
    ProfileDetailView,
    SkillListView,
    ExperienceListView,
    EducationListView,
    ProjectListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectManageView,
    CategoryListView,
    TagListView,
    PostListView,
    PostDetailView,
    ContactMessageCreateView,
)

urlpatterns = [
    # Profile API
    path("profile/", ProfileDetailView.as_view(), name="profile"),

    # Skills API
    path("skills/", SkillListView.as_view(), name="skills"),

    # Experience API
    path("experience/", ExperienceListView.as_view(), name="experience"),

    # Education API
    path("education/", EducationListView.as_view(), name="education"),

    # Public Project API
    path("projects/", ProjectListView.as_view(), name="projects"),

    # Create Project API
    path(
        "projects/create/",
        ProjectCreateView.as_view(),
        name="project-create",
    ),

    # Update or Delete Project API
    path(
        "projects/<slug:slug>/manage/",
        ProjectManageView.as_view(),
        name="project-manage",
    ),

    # Project Details API
    path(
        "projects/<slug:slug>/",
        ProjectDetailView.as_view(),
        name="project-detail",
    ),

    # Category API
    path("categories/", CategoryListView.as_view(), name="categories"),

    # Tag API
    path("tags/", TagListView.as_view(), name="tags"),

    # Blog Post API
    path("posts/", PostListView.as_view(), name="posts"),

    # Blog Post Details API
    path(
        "posts/<slug:slug>/",
        PostDetailView.as_view(),
        name="post-detail",
    ),

    # Contact API
    path(
        "contact/",
        ContactMessageCreateView.as_view(),
        name="contact",
    ),
]