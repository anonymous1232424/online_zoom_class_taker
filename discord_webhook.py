from discord_webhook import DiscordWebhook, DiscordEmbed

# Put your webhook url .
webhook_url = ""


def send_message(class_name, status, joined_time, end_time):
    webhook = DiscordWebhook(webhook_url)

    # Checking for status Joined .
    if status == "Joined":
        # Making an Embed Object .
        embed_joined = DiscordEmbed(title='Class Joined Successfully',
                                    description="Here's your report with :heart:")

        # Adding fields to the objects !
        embed_joined.add_embed_field(name='Class', value=class_name)
        embed_joined.add_embed_field(name='Status', value=status)
        embed_joined.add_embed_field(name='Joined At', value=joined_time)
        embed_joined.add_embed_field(name='Leaving At', value=end_time)

        webhook.add_embed(embed_joined)
        # Sending the message .
        webhook.execute()

    # Checking for status Left .
    elif status == "Left":
        embed_left = DiscordEmbed(title='Class Left Successfully',
                                  description="Here's your report with :heart:")

        embed_left.add_embed_field(name='Class', value=class_name)
        embed_left.add_embed_field(name='Status', value=status)
        embed_left.add_embed_field(name='Left At', value=end_time)

        webhook.add_embed(embed_left)
        webhook.execute()
