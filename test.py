#!/usr/bin/env python
# coding: utf-8

# In[1]:


from wallet import Wallet
def test_getAmount():
    obj=Wallet()
    obj.setAmount(20)
    assert obj.getAmount==20


# In[ ]:




