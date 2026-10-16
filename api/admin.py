from django.contrib import admin

from .models import (
    Profile,
    Skill,
    Experience,
    Education,
    Project,
    Category,
    Tag,
    Post,
    PostLike,
    Comment,
    ContactMessage,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "headline", "email")
    search_fields = ("full_name", "headline", "email")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "display_order")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("position", "company", "start_date", "is_current")
    list_filter = ("is_current",)
    search_fields = ("position", "company")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "field_of_study")
    search_fields = ("degree", "institution")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "created_at")
    list_filter = ("is_featured",)
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "status", "published_at")
    list_filter = ("status", "category", "tags")
    search_fields = ("title", "content")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)


@admin.register(PostLike)
class PostLikeAdmin(admin.ModelAdmin):
    list_display = ("post", "user", "created_at")
    search_fields = ("post__title", "user__username")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "post", "is_approved", "created_at")
    list_filter = ("is_approved", "created_at")
    search_fields = ("name", "email", "content")


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "subject", "email", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject")