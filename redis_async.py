import redis.asyncio as redis
import httpx
import config

redis_client = redis.Redis(
    host=config.HOST,
    port=config.PORT,
    decode_responses=True,
    username="default",
    password=config.PASSWORD
)

async def isRegistered(chat_id:int, url:str):
    if await redis_client.exists(str(chat_id)):
        return True
    else:
        isAdded = await getContactBitrix(chat_id, url)
        if isAdded:
            await redis_client.set(str(chat_id), 1, ex=43200)
            return True
        else:
            return False

async def getContactBitrix(chat_id:int, url:str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f'{url}/crm.contact.list?filter[UF_CRM_CHAT_ID]={chat_id}'
            )
        except httpx.RequestError as e:
            return await getContactBitrix(chat_id, url)
        else:
            json_data = response.json()
            result = json_data.get('result', [])
            return False if not result else True