require File.dirname(File.expand_path(__FILE__)) + '/../spec_helper'

describe Spira::Types::List do
 
  context "when serializing" do
    it "should serialize arrays to `RDF.List`s" do
      serialized = Spira::Types::List.serialize([1,2,3])
      serialized.should be_a RDF::List
      serialized.should == RDF::List[1,2,3]
    end

    it "should serialize other types to `RDF.List`s" do
      serialized = Spira::Types::List.serialize(1)
      serialized.should be_a RDF::List
      serialized.should == RDF::List[1]
    end
  end

  context "when unserializing" do
    it "should unserialize RDF Lists to arrays" do
      value = Spira::Types::List.unserialize(RDF::List[1,2,3])
      value.should be_a Array
      value.should == [1,2,3]
    end

    it "should unserialize anything else to an array" do
      value = Spira::Types::List.unserialize(RDF::Literal.new(5, :datatype => RDF::XSD.integer))
      value.should be_a Array
      value.should == [5]
    end

    it "should unserialize nested RDF Lists to arrays" do
      nested = Spira::Types::List.unserialize(RDF::List[1,2,[3,4,5],[6,[7,8,9]]])
      nested.should be_a Array
      nested.should == [1,2,[3,4,5],[6,[7,8,9]]]
    end
  end

end
