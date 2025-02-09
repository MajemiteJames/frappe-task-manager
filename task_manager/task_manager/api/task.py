import frappe
from frappe import _
from frappe.utils import redis_cache

# Redis cache key prefix
CACHE_KEY_PREFIX = "task_"

@frappe.whitelist()
def create_task(title, description, status="Open"):
    task = frappe.get_doc({
        "doctype": "Task",
        "title": title,
        "description": description,
        "status": status
    })
    task.insert()
    return task.name

@frappe.whitelist()
def get_task(task_name):
    # Check if the task is cached
    cache_key = f"{CACHE_KEY_PREFIX}{task_name}"
    task = redis_cache.get(cache_key)

    # If not cached, fetch from the database and cache it
    if not task:
        task = frappe.get_doc("Task", task_name)
        redis_cache.set(cache_key, task)
    return task

@frappe.whitelist()
def update_task(task_name, title=None, description=None, status=None):
    task = frappe.get_doc("Task", task_name)
    if title:
        task.title = title
    if description:
        task.description = description
    if status:
        task.status = status
    task.save()

    # Update the cache
    cache_key = f"{CACHE_KEY_PREFIX}{task_name}"
    redis_cache.set(cache_key, task)
    return task.name

@frappe.whitelist()
def delete_task(task_name):
    # Delete the task from the database
    frappe.delete_doc("Task", task_name)

    # Clear the cache
    cache_key = f"{CACHE_KEY_PREFIX}{task_name}"
    redis_cache.delete(cache_key)
    return _("Task deleted successfully")