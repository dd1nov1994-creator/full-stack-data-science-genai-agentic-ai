{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "91b77cba-bdfa-4334-9df6-abc8c570931a",
   "metadata": {},
   "outputs": [],
   "source": [
    "#TOKENIZATION OF PARAGRAPHS/SENTENCES\n",
    "import nltk"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "42f41712-75c5-42f6-ba92-5ffbb5f3a8a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "paragraph = \"\"\"I have three visions for India. In 3000 years of our history, people from all over \n",
    "               the world have come and invaded us, captured our lands, conquered our minds. \n",
    "               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,\n",
    "               the French, the Dutch, all of them came and looted us, took over what was ours. \n",
    "               Yet we have not done this to any other nation. We have not conquered anyone. \n",
    "               We have not grabbed their land, their culture, \n",
    "               their history and tried to enforce our way of life on them. \n",
    "               Why? Because we respect the freedom of others.That is why my \n",
    "               first vision is that of freedom. I believe that India got its first vision of \n",
    "               this in 1857, when we started the War of Independence. It is this freedom that\n",
    "               we must protect and nurture and build on. If we are not free, no one will respect us.\n",
    "               My second vision for India’s development. For fifty years we have been a developing nation.\n",
    "               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world\n",
    "               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.\n",
    "               Our achievements are being globally recognised today. Yet we lack the self-confidence to\n",
    "               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?\n",
    "               I have a third vision. India must stand up to the world. Because I believe that unless India \n",
    "               stands up to the world, no one will respect us. Only strength respects strength. We must be \n",
    "               strong not only as a military power but also as an economic power. Both must go hand-in-hand. \n",
    "               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of \n",
    "               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.\n",
    "               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. \n",
    "               I see four milestones in my career. india is great compare to other country. \"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1f5773f6-bbb8-41e9-ad82-e7fe32989132",
   "metadata": {},
   "outputs": [],
   "source": [
    "#TOKENIZING SENTENCES\n",
    "sentences = nltk.sent_tokenize(paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1c60dcd3-3f36-471b-99fb-0385565155b7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#TOKENIZING WORDS\n",
    "words = nltk.word_tokenize(paragraph)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "42b3c54d-6b92-4e78-9170-21c26b3b36cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#STEMMING\n",
    "from nltk.stem import PorterStemmer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "c894b4b4-1e03-4a69-ad5c-d905534ea8ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.corpus import stopwords"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "be4e24fb-52fa-4a37-af68-27a9f47767e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "stemmer = PorterStemmer()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "611cbd5c-1860-4587-866b-8ba1317524ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(sentences)):\n",
    "    words = nltk.word_tokenize(sentences[i])\n",
    "    words = [stemmer.stem(word) for word in words if word not in set(stopwords.words('english')) ]\n",
    "    sentences[i] = ' '.join(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "a034b187-55e5-4a81-9db4-a474b15bb331",
   "metadata": {},
   "outputs": [],
   "source": [
    "#LEMMATIZATION\n",
    "from nltk.stem import WordNetLemmatizer"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "187f19fb-2e84-4d50-9ea0-88787750b49b",
   "metadata": {},
   "outputs": [],
   "source": [
    "from nltk.corpus import stopwords    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "2163d090-2eef-416c-bd88-5f1b5d9d4679",
   "metadata": {},
   "outputs": [],
   "source": [
    "lemmatizier = WordNetLemmatizer() "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "53799a9a-f923-45c9-8d12-e348091e6cac",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(sentences)):\n",
    "    words = nltk.word_tokenize(sentences[i])\n",
    "    words = [lemmatizier.lemmatize(word) for word in words if word not in set(stopwords.words('english')) ]\n",
    "    sentences[i] = ' '.join(words)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fc9ea0d-e893-429b-b273-cfd5b5df0586",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
