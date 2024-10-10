from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper

app = FastAPI()


@app.post("/")
async def handle_request(request: Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload ['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    
    if intent == "total.spent":
        return view_spend(parameters)
    if intent == "view.status":
        return view_status(parameters)
    if intent == "actual.edit.budget":
        return edit_budget(parameters)
    if intent == "actual.edit.status":
        return edit_status(parameters)
    if intent == "view-actual-budget":
        return view_budget(parameters)
    

def view_budget(parameters: dict):
    campaign_name = parameters["campaign-name"]
    budget = db_helper.view_budget(campaign_name)
    
    if budget:
        fulfillment_text = f"The total budget of Campaign: {campaign_name} is: {budget}"
    else:
        fulfillment_text = f"No Campaign with campaign name : {campaign_name}"
    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })

def edit_status(parameters: dict):
    campaign_name = parameters["campaign-name"]
    status = parameters["status"]
    db_helper.edit_status(campaign_name,status)
    
    fulfillment_text = f"Successfully updated the status for campaign {campaign_name} to {status}"
    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })
     
    
def edit_budget(parameters: dict):
    campaign_name = parameters["campaign-name"]
    budget = parameters["number-integer"]
    db_helper.edit_budget(campaign_name,budget)
    
    fulfillment_text = f"Successfully updated the budget for campaign {campaign_name} to {budget}"
    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })
    
    
def view_spend(parameters: dict):
    campaign_name = parameters["campaign-name"]
    totalSpend = db_helper.view_total_spend(campaign_name)
    
    if totalSpend:
        fulfillment_text = f"The total Spend of Campaign: {campaign_name} is: {totalSpend}"
    else:
        fulfillment_text = f"No Campaign with campaign name : {campaign_name}"
    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })

def view_status(parameters: dict):
    campaign_name = parameters["campaign-name"]
    totalSpend = db_helper.view_current_status(campaign_name)
    
    if totalSpend:
        fulfillment_text = f"The current Status of Campaign: {campaign_name} is: {totalSpend}"
    else:
        fulfillment_text = f"No Campaign with campaign name : {campaign_name}"
    
    return JSONResponse(content={
            "fulfillmentText": fulfillment_text
        })


