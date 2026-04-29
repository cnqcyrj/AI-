# tests/test_deploy.py
import subprocess
import unittest

class TestDeploy(unittest.TestCase):

    def test_deploy_to_heroku(self):
        """测试部署到 Heroku"""
        result = subprocess.run(["git", "push", "heroku", "main"], capture_output=True, text=True)
        self.assertIn("Everything up-to-date", result.stdout)

    def test_deploy_to_aws(self):
        """测试部署到 AWS"""
        result = subprocess.run(["aws", "deploy", "push", "--application-name", "myapp", "--s3-location", "myapp.zip"], capture_output=True, text=True)
        self.assertIn("Successfully deployed", result.stdout)

    def test_deploy_to_gcp(self):
        """测试部署到 GCP"""
        result = subprocess.run(["gcloud", "app", "deploy"], capture_output=True, text=True)
        self.assertIn("Deployment successful", result.stdout)

if __name__ == "__main__":
    unittest.main()
