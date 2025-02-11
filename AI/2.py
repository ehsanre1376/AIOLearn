#%%

import requests as req


# %%
s=input("Ask : ")
ans= req.get("https://5.161.91.18/chat?text=" + s)


# %%
print(ans.json())