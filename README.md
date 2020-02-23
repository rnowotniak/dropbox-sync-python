## Backup to Dropbox, Linux script

What is supposed to do:

* Demo and test OAuth2 protocol
* Use "implicit grant" method

Allow to make files backups in your Dropbox in the application folder.

1)  code grant (server side / web apps)  /  both key & secret  / 2 stages  (more secure)
    (can be guaranteed that the user will not view the source code to get the key & the secret)
    The rationale is to never expose secret to the user, thus they can't pretend to be the same app.
    1)  step one - just to authenticate 
    2)  step two -  to exchange the authorization code to token

2)  implicit grant - token (client side,  mobile / JS)  /  app key only  / 1 stage
    User can view the source code (JS), no reaseon to distinguish between public key & secret

Token is like a key to access the files (bearer token).

In this project, it makes sense to use Option 2.


* https://www.dropbox.com/developers/reference/oauth-guide
* https://blogs.dropbox.com/developers/2013/07/using-oauth-2-0-with-the-core-api/
* https://www.dropboxforum.com/t5/API-Support-Feedback/API-secret-in-dropbox-oauth-DropboxOAuth2FlowNoRedirect-and/td-p/276987
* https://www.quora.com/Why-does-OAuth-server-return-a-authorization-code-instead-of-access-token-in-the-first-step
* https://www.digitalocean.com/community/tutorials/an-introduction-to-oauth-2
* https://www.dropbox.com/developers/reference/oauth-guide

