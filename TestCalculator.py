import json

def lambda_handler(event, context):

    print("Starting the Calculator App")
    var1 = int(event['key1'])
    var2 = int(event['key2'])
    print("Operators are: ",var1," and ",var2)
    var4 = event['key3'][0]
    print("Operand is: ",var4)
    if var4 == '+':
        print(var1+var2)
    elif var4 == '-':
        print(var1-var2)
    elif var4 == '*':
        print(var1*var2)
    else:
        print(var1/var2)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
