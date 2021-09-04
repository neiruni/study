from .models import M_Items, M_Users
from django.db.models import Q


class SearchView():
    def fruits_search(object):
        item_no = object['item_no']
        item_nm = object['item_nm']
        register_from = object['register_from']
        register_to = object['register_to']

        condition_item_no = Q()
        condition_item_nm = Q()
        condition_register_from = Q()
        condition_register_to = Q()
        condition_del_flg = Q()


        if len(item_no) != 0:
            condition_item_no = Q(item_no__iexact=item_no)

        if len(item_nm) != 0:
            condition_item_nm = Q(item_nm__istartswith=item_nm)
        
        if len(register_from) != 0:
            condition_register_from = Q(register_dt__gte=register_from)

        if len(register_to) != 0:
            condition_register_to = Q(register_dt__lte=register_to)
        
        condition_del_flg = Q(del_flg=1)

        object_list = M_Items.objects.select_related().filter(condition_item_no & condition_item_nm & condition_register_from & condition_register_to & condition_del_flg)

        return object_list
    
    def user_search(object):
        user_id = object['user_id']
        user_name = object['user_name']
        del_flg = object['del_flg']

        condition_user_id = Q()
        condition_user_name = Q()
        condition_del_flg = Q()

        if len(user_id) != 0:
            condition_user_id = Q(user_id__iexact=user_id)

        if len(user_name) != 0:
            condition_user_name = Q(user_name__istartswith=user_name)
        
        if len(del_flg) != 0:
            condition_del_flg = Q(del_flg=del_flg)

        object_list = M_Users.objects.select_related().filter(condition_user_id & condition_user_name & condition_del_flg)

        return object_list
